using Microsoft.WindowsAzure.Storage;
using Microsoft.WindowsAzure.Storage.Queue;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.IO;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace HackDayUploader.Controllers
{
    public class HomeController : Controller
    {
        private CloudStorageAccount StorageAccount;
        private string BlobContainer = "hackbaseball";
        private string DestinationFolder = "uploads";

        public HomeController()
        {
            var storageConnectionString = ConfigurationManager.AppSettings.Get("StorageAccountConnectionString");
            StorageAccount = CloudStorageAccount.Parse(storageConnectionString);
        }

        public ActionResult Index()
        {
            return View();
        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }

        public class ViewDataUploadFilesResult
        {
            public string Name { get; set; }
            public int Length { get; set; }
        }

        public ActionResult Upload(string park, string date)
        {
            var r = new List<ViewDataUploadFilesResult>();

            foreach (string file in Request.Files)
            {
                HttpPostedFileBase hpf = Request.Files[file] as HttpPostedFileBase;
                if (hpf.ContentLength == 0)
                    continue;
                string savedFileName = Path.Combine(
                   AppDomain.CurrentDomain.BaseDirectory,
                   Path.GetFileName(hpf.FileName));
                //hpf.SaveAs(savedFileName);

                UploadToAzure(hpf.FileName, hpf.InputStream);
                AddToQueue(hpf.FileName, park, date);

                r.Add(new ViewDataUploadFilesResult()
                {
                    Name = hpf.FileName,
                    Length = hpf.ContentLength
                });
            }
            return View("UploadedFiles", r);
        }

        private void AddToQueue(string imageName, string park, string date)
        {
            var queueClient = StorageAccount.CreateCloudQueueClient();
            var queue = queueClient.GetQueueReference("hackbaseball");
            var content = String.Format("{0}|{1}|{2}", imageName, park, date);
            queue.AddMessage(new CloudQueueMessage(content));
        }

        private void UploadToAzure(string fileName, Stream dataStream)
        {
            // finally add a prefix to indicate the file hasn't been processed
            var blobClient = StorageAccount.CreateCloudBlobClient();
            var container = blobClient.GetContainerReference(BlobContainer);
            var blob = container.GetBlockBlobReference(fileName);
//            blob.Properties.ContentType = "application/xml";
            blob.UploadFromStream(dataStream);
        }
    }
}