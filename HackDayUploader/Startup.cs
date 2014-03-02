using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(HackDayUploader.Startup))]
namespace HackDayUploader
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
