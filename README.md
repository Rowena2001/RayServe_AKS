# Ray Serve AKS Exploration

# Introduction 

[**Ray Serve**](https://docs.ray.io/en/latest/serve/index.html) is a scalable and framework-agnostic model serving library that allows developers to build online inference APIs with Python. Serve is built on top of Ray, so it easily scales to many machines and offers flexible scheduling support such as fractional GPUs so you can share resources and serve many machine learning models at low cost. Ray Serve can run on any Kubernetes cluster using [**KubeRay**](https://ray-project.github.io/kuberay/), providing the benefits of both Ray's scalable serving and Kubernetes' operational features.

In this project, we will explore how to use **Ray Serve** on **Azure Kubernetes Service (AKS)** to deploy deep learning models. We will start by deploying a simple "Hello World" service on AKS using Ray Serve and the KubeRay operator. Then, we will deploy a Hugging Face model on AKS using Ray Serve and the KubeRay operator. Finally, we will explore how to autoscale the Hugging Face model using Ray Serve and the KubeRay operator.

# About this Repository

This repository contains configuration files for deploying models on Ray Serve and AKS. These configuration files use Ray deployment code from the [Final_Deployments](https://github.com/Rowena2001/Final_Deployments) repo as the working directory.

# Project Summary

This project consisted of five MVPs, each geared towards exploring deeper into the capabilities of Ray Serve on AKS. The first MVP was to deploy a simple **Hello World application** on AKS using Ray Serve and the KubeRay operator. The second MVP was to deploy a **Hugging Face model** on AKS using Ray Serve and the KubeRay operator. The third MVP was to deploy a Hugging Face model on AKS using Ray Serve and the KubeRay operator with **autoscaling**. The fourth MVP was to create an **automated pipeline** to create deployments and make them available for configuration. The fifth MVP was to integrate all components of the project into a cohesive **demonstration**.

## MVP1: Deploying a Hello World Application on Ray Serve and AKS
- Learning Outcomes:
    - Familiarize with Ray Serve, Kubernetes/AKS, and KubeRay
    - Deploy a simple application on Ray Serve locally (without Kubernetes/AKS)
    - Deploy a simple application on Ray Serve on Kubernetes using KubeRay (kind)
    - Deploy a simple application on Ray Serve and AKS using KubeRay
    - How to port-forward services to local machine
    - How to query services using curl
    - How to use the open-source community for troubleshooting
- Issues Encountered:
    - Runtime Environment Working Directory: When configuring a Ray Serve deployment on AKS with KubeRay, the "runtimeEnv/working_dir" field must be a publicly accessible link. Using a local file path will not work as the KubeRay operator does not support this. This issue was resolved by uploading the working directory to a public GitHub repository and using the release zip file link as the runtimeEnv. Here is an example of the runtimeEnv field:
    ```
    runtimeEnv: |
        {"working_dir": "https://github.com/Rowena2001/Final_Deployments/archive/refs/tags/latest.zip"}
    ```
## MVP2: Deploying a Hugging Face Model on Ray Serve and AKS
- Learning Outcomes:
    - Familiarize with Hugging Face Transformers pipeline
    - Deploy a Hugging Face model on Ray Serve locally (without Kubernetes/AKS)
    - Deploy a Hugging Face model on Ray Serve on AKS using KubeRay
    - How to edit a KubeRay configuration file to customize resources (CPU, GPU, memory)
    - How to port-forward and view the Ray Serve dashboard
- Issues Encountered:
    - Runtime Environment Dependencies: Include dependencies like pip packages in the runtimeEnv field to ensure that the model can be deployed. Use a conda environment to check which package versions are compatible with your Python environment. Here is an example of the runtimeEnv field with dependencies:
    ```
    runtimeEnv: |
      {"working_dir": "https://github.com/Rowena2001/Final_Deployments/archive/refs/tags/latest.zip", 
      "pip": ["torch==1.13.1", "transformers==4.30.2", "accelerate==0.20.3"]}
    ```
    - Hugging Face Accelerate Device Map: When using GPU resources with a Hugging Face model, use Accelerate's device map in the Transformers pipeline to detect GPU devices. Here is an example of using device map in the Transformers pipeline:
    ```
    model = pipeline("translation_en_to_fr", model="t5-small", device_map="auto")
    ```
    - GPU Image: When configuring a Ray Serve deployment to use GPU resources, a GPU Ray docker image like "rayproject/ray-ml:2.5.0-gpu" must be used. Using a normal Ray docker image like "rayproject/ray:2.5.0" will not work as the image does not have GPU support.
    - Sufficient Resources: Ensure that each pod has sufficient resources to support the application. If the pod does not have sufficient resources, the pod will be stuck in the "Pending" state and the model will not be deployed. This issue was resolved by increasing the CPU and memory resources in the KubeRay configuration file.

## MVP3: Deploying a Hugging Face Model on Ray Serve and AKS with Autoscaling
- Learning Outcomes:
    - Familiarize with the concept of autoscaling
    - Deploy a model on Ray Serve with autoscaling locally using autoscaling_config (without Kubernetes/AKS)
    - Deploy a model on Ray Serve with autoscaling on AKS using KubeRay
    - How to edit a KubeRay configuration file to customize autoscaling parameters
    - How to use Prometheus and Grafana to monitor the Ray cluster
    - How to file an issue on GitHub to contribute to the open-source community
- Issues Encountered:
    - Autoscaling Configuration: When configuring Ray Serve autoscaling on AKS using KubeRay, the autoscalingConfig field is not supported in the YAML configuration file. This issue was resolved by using the autoscaling_config field in the Ray Serve deployment code. Refer to [Set Up Autoscaling and Resource Allocation](https://docs.ray.io/en/master/serve/scaling-and-resource-allocation.html#) for more information. Here is an example of the autoscaling_config field in Python:
    ```
    @serve.deployment(
        autoscaling_config={
            "min_replicas": 2,
            "initial_replicas": 2,
            "max_replicas": 10,
            "upscale_delay_s": 5,
        }
    )
    class ClassName:
        # deployment class code
    ```
    - HTTP Proxy Actors Crashing when Upscaling: When a Ray Serve deployment is upscaling, the HTTP proxy actors may crash and restart with older version of KubeRay. This issue was resolved by using the nightly release of KubeRay. Refer to (this issue)[https://github.com/ray-project/kuberay/issues/1222] for more information.

## MVP4: Automated Pipeline
- Learning Outcomes:
    - Familiarize with GitHub Actions
    - Configure a GitHub Actions workflow to automate release creation
## MVP5: Demonstration
- Learning Outcomes:
    - Create a comprehensive presentation to demonstrate the learning outcomes and milestones of the project
    - Demonstrate the deployment of a Hugging Face model on Ray Serve and AKS with autoscaling

# Ray Serve on AKS Tutorials
## MVP1: Deploying a Hello World Application on Ray Serve and AKS

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

## MVP2: Deploying a Hugging Face Model on Ray Serve and AKS

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

## MVP3: Deploying a Hugging Face Model on Ray Serve and AKS with Autoscaling

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

## MVP4: Developing an Automated Pipeline for Releases

To make Ray deployments accessible for KubeRay configuration, a publicly available release is needed for the working directory. This can be done by creating a release on GitHub. To automate release creation, a pipeline can be used to create a release whenever something is pushed to the repository. This can be done using GitHub Actions. Follow (GitHub Docs)[https://docs.github.com/en/actions/using-workflows/triggering-a-workflow] to learn more about creating a workflow file. The following is an example of a workflow file that creates a "latest" release whenever something pushed to the repository.

```
name: "auto-release"

on:
  push:
    branches:
      - "master"

jobs:
  auto-release:
    name: "Auto Release"
    permissions: write-all
    runs-on: "ubuntu-latest"

    steps:
    - name: Automatic Releases
      uses: marvinpinto/action-automatic-releases@v1.2.1
      with:
        repo_token: "${{ secrets.GITHUB_TOKEN }}"
        automatic_release_tag: "latest"
        title: "Development Build"
```

## Viewing the Ray Dashboard on AKS

1. Get the Ray cluster name using kubectl.
```
kubectl get rayclusters
```
2. View the Ray dashboard by port-forwarding it to your local machine.
```
kubectl port-forward --address 0.0.0.0 service/${RAYCLUSTER_NAME}-head-svc 8265:8265 
```
3. Access the dashboard on your browser at localhost:8265.