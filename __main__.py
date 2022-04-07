"""A Kubernetes Python Pulumi program"""

import os
import pulumi
from pulumi_kubernetes.apps.v1 import Deployment, DeploymentSpecArgs
from pulumi_kubernetes.meta.v1 import LabelSelectorArgs, ObjectMetaArgs
from pulumi_kubernetes.core.v1 import ContainerArgs, PodSpecArgs, PodTemplateSpecArgs
from models.nginx import Nginx

ENV = os.environ.get('PULUMI_ENV')

app_labels = { "app": "nginx" }

nginx = Nginx('nginx', 'nginx', app_labels, app_labels)
nginx.build(ENV)

deployment = Deployment(
    "nginx",
    spec=DeploymentSpecArgs(
        selector=LabelSelectorArgs(match_labels=nginx.match_labels),
        replicas=nginx.replicas,
        template=PodTemplateSpecArgs(
            metadata=ObjectMetaArgs(labels=nginx.labels),
            spec=PodSpecArgs(containers=[ContainerArgs(name=nginx.name, image=nginx.image)])
        ),
    ))

pulumi.export("name", deployment.metadata["name"])
