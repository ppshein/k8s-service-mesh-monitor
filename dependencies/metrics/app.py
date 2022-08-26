import json
from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException
from kubernetes.client.api_client import ApiClient
from kubernetes import client, config


def main():
    config.load_incluster_config()

    v1 = client.CoreV1Api()
    api_client = ApiClient()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        ret_metrics = api_client.call_api('/apis/metrics.k8s.io/v1beta1/pods/' + i.metadata.name, 'GET', auth_settings = ['BearerToken'], response_type='json', _preload_content=False) 
        response = ret_metrics[0].data.decode('utf-8')
        print(response)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        if "Forbidden" or "Unauthorized" in e:
            print("Unauthorized. Please make sure to login to the cluster and that you have permission")
        else:
            print(e)