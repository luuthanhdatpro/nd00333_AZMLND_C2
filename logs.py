from azureml.core import Workspace
from azureml.core.webservice import Webservice


ws = Workspace.get(
    name="quick-starts-ws-269435",
    subscription_id="61c5c3f0-6dc7-4ed9-a7f3-c704b20e3b30",
    resource_group="aml-quickstarts-269435",
    # auth=sp_auth
)
# Requires the config to be downloaded first to the current working directory
# ws = Workspace.from_config()

# Set with the deployment name
name = "banking1"

# load existing web service
service = Webservice(name=name, workspace=ws)

service.update(enable_app_insights=True)

logs = service.get_logs()

for line in logs.split('\n'):
    print(line)
