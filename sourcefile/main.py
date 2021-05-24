#  EC2 creation using python boto3

import boto3
def create_ec2_instances():
    try:
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-00399ec92321828f5",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="mainkey"
        )
    except Exception as e:
        print(e)

def describe_ec2_instance():
    try:
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
    except Exception as e:
        print(e)

def reboot_ec2_instance():
    try:
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.reboot_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

def stop_ec2_instance():
    try:
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.stop_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

def start_ec2_instance():
    try:
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.start_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

def terminate_ec2_instance():
    try:
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

terminate_ec2_instance()
#start_ec2_instance()
#stop_ec2_instance()
#reboot_ec2_instance()
#describe_ec2_instance()

#create_ec2_instances()