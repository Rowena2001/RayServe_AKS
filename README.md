# Ray Serve AKS Exploration

This is a repository for exploring the deployment of models on Ray Serve and AKS. The goal is to create a pipeline that can be used to deploy models on AKS using Ray Serve with autoscaling.

## Ray Serve on AKS Tutorials

### MVP1: Deploying a Hello World Application on Ray Serve and AKS

1. If you don't already have an AKS cluster, follow AKS documentation to create one.
2. Install Ray Serve using pip.
```
pip install "ray[serve]"
```
3. Follow [Deploying Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html#kuberay-quickstart) documentation to install kubectl and Helm.
4. Deploy the KubeRay operator. Please not that the KubeRay nightly release is best for autoscaling as the stable release has a bug (refer to Issues Encountered).
```
# Stable release
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm install kuberay-operator kuberay/kuberay-operator --version 0.5.0

# Nightly release
git clone https://github.com/ray-project/kuberay.git
cd kuberay/helm-chart/kuberay-operator
helm install kuberay-operator . --set image.repository=kuberay/operator,image.tag=nightly
```
5. Apply helloworld_config.yaml file to the cluster.
```
kubectl apply -f helloworld_config.yaml
```
6. Check pods and services using kubectl.
```
kubectl get pods
kubectl get services
```
7. Forward the Ray Serve dashboard and helloworld service to your local machine.
```
# Get the name of the Ray cluster
kubectl get rayclusters
kubectl port-forward --address 0.0.0.0 service/${RAYCLUSTER_NAME}-head-svc 8265:8265 
# Access the dashboard on your browser at localhost:8265
```
8. Forward the helloworld service to your local machine.
```
kubectl port-forward service/helloworld-serve-svc 8000
# Access the service on your browser at localhost:8000 or using curl localhost:8000
```

### MVP2: Deploying a Hugging Face Model on Ray Serve and AKS

1. If you don't already have an AKS cluster, follow AKS documentation to create one.
2. Install transformers using pip.
```
pip install transformers
```
3. Follow [Deploying Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html#kuberay-quickstart) documentation to install kubectl and helm.
4. Deploy the KubeRay operator. Please not that the KubeRay nightly release is best for autoscaling as the stable release has a bug (refer to Issues Encountered).
```
# Stable release
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm install kuberay-operator kuberay/kuberay-operator --version 0.5.0

# Nightly release
git clone https://github.com/ray-project/kuberay.git
cd kuberay/helm-chart/kuberay-operator
helm install kuberay-operator . --set image.repository=kuberay/operator,image.tag=nightly
```
5. Apply model_cpu_config.yaml or model_gpu_config.yaml file to the cluster depending on what resources you would like to use.
```
kubectl apply -f model_cpu_config.yaml
kubectl apply -f model_gpu_config.yaml
```
6. Check pods and services using kubectl.
```
kubectl get pods
kubectl get services
```
7. Forward the Ray Serve dashboard and helloworld service to your local machine.
```
# Get the name of the Ray cluster
kubectl get rayclusters
kubectl port-forward --address 0.0.0.0 service/${RAYCLUSTER_NAME}-head-svc 8265:8265 
# Access the dashboard on your browser at localhost:8265
```
8. Forward the translator-model service to your local machine.
```
kubectl port-forward service/translator-model-serve-svc 8000
```
9. Run a model_client script to access the service.
```
python clients/model_client_medium.py
python clients/model_client_multithread.py
```

### MVP3: Deploying a Hugging Face Model on Ray Serve and AKS with Autoscaling

1. If you don't already have an AKS cluster, follow AKS documentation to create one.
2. Install transformers using pip.
```
pip install transformers
```
3. Follow [Deploying Ray on Kubernetes](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started.html#kuberay-quickstart) documentation to install kubectl and helm.
4. Deploy the Kuberay operator. Please not that the Kuberay nightly release is best for autoscaling as the stable release has a bug (refer to Issues Encountered).
```
# Stable release
helm repo add kuberay https://ray-project.github.io/kuberay-helm/
helm install kuberay-operator kuberay/kuberay-operator --version 0.5.0

# Nightly release
git clone https://github.com/ray-project/kuberay.git
cd kuberay/helm-chart/kuberay-operator
helm install kuberay-operator . --set image.repository=kuberay/operator,image.tag=nightly
```
5. Apply model_cpu_config.yaml or model_gpu_config.yaml file to the cluster depending on what resources you would like to use.
```
kubectl apply -f model_autoscale_config.yaml
```
6. Check pods and services using kubectl.
```
kubectl get pods
kubectl get services
```
7. Forward the Ray Serve dashboard and helloworld service to your local machine.
```
# Get the name of the Ray cluster
kubectl get rayclusters
kubectl port-forward --address 0.0.0.0 service/${RAYCLUSTER_NAME}-head-svc 8265:8265 
# Access the dashboard on your browser at localhost:8265
```
8. Forward the translator-autoscale service to your local machine.
```
kubectl port-forward service/translator-autoscale-serve-svc 8000
```
9. Run a model_client script to access the service.
```
python clients/model_client_medium.py
python clients/model_client_multithread.py
```

### Viewing the Ray Dashboard on AKS

1. Get the Ray cluster name using kubectl.
```
kubectl get rayclusters
```
2. View the Ray dashboard by port-forwarding it to your local machine.
```
kubectl port-forward --address 0.0.0.0 service/${RAYCLUSTER_NAME}-head-svc 8265:8265 
```
3. Access the dashboard on your browser at localhost:8265.

## Issues Encountered

### runtimeEnv
1. The field "working_dir" does not work for local files. Therefore, one must use a link to a github repository.
2. Include dependencies in the runtimeEnv. For example, include the field "pip" to install packages using pip.
Use the following example as a template.
```
runtimeEnv: |
    {"working_dir": "https://github.com/Rowena2001/Final_Deployments/archive/refs/tags/1.0.zip", 
    "pip": ["torch==1.13.1", "transformers==4.30.2"]}
```

### autoscalingConfig
Ray Serve offers autoscaling for deployments by increasing and decreasing number of replicas based on the number of requests.
Currently, the autoscalingConfig field must be included in the python source code as a deployment parameter.
The autoscalingConfig field is not supported in the yaml file for apiVersion ray.io/v1alpha1 and serveConfig.
Refer to [Set Up Autoscaling and Resource Allocation](https://docs.ray.io/en/master/serve/scaling-and-resource-allocation.html#) for more information.

### serveConfig2
serveConfig2 is supported by KubeRay v0.5.2 and nightly release.
When uninstalling KubeRay stable version and installing KubeRay nightly version, ensure to manually change CRD's as helm uninstall does not remove them.
Refer to [this issue](https://github.com/ray-project/kuberay/issues/1194) and [this issue](https://github.com/ray-project/kuberay/issues/1216) for more information.

### autoscaling on AKS and port-forwarding
When autoscaling is enabled and the service is port-forwarded to the local machine, multithreaded queries might cause a connection error.
Steps to solve this issue:
1. Use KubeRay nightly release.
2. Ensure ray[default] is installed or added as an environment dependency in the configuration file.
3. Restart the service using the 'kubectl port-forward' command.
Refer to [this issue](https://github.com/ray-project/kuberay/issues/1222) for more information.