import boto3
from botocore.exceptions import ClientError
ec2=boto3.resource("ec2")

def start_instance(instance_ids):
    try:
      ec2.instances.filter(InstanceIds=instance_ids).start()
      print(f"started instances : {instance_ids}")
    except ClientError as e:
        print(f"error occured {e}")

def stop_instance(instance_ids):
    try:
     ec2.instances.filter(InstanceIds=instance_ids).stop()
     print(f"stopped instances are : {instance_ids}")
    except ClientError as e:
      print(f"error occured {e}")
def terminate_instance(instance_ids):
    try:
     ec2.instances.filter(InstanceIds=instance_ids).terminate()
     print(f"terminated instances are {instance_ids}")
    except ClientError as e:
       print(f"error occured {e}")
def reboot_instance(instance_ids):
    try:
     ec2.instances.filter(InstanceIds=instance_ids).reboot()
     print(f"terminated instances are {instance_ids}")
    except ClientError as e:
      print(f"error occured as {e}")
def main():
    while True:
        print("\nChoose an action:")
        print("1. Start Instances")
        print("2. Stop Instances")
        print("3. Reboot Instances")
        print("4. Terminate Instances")
        print("5. Exit")

      
        choice = input("Enter choice: ")

        if choice == '5':
            break

        instance_ids = input("Enter instance IDs separated by commas: ").split(',')


        if choice == '1':
            start_instance(instance_ids)
        elif choice == '2':
            stop_instance(instance_ids)
        elif choice == '3':
            reboot_instance(instance_ids)
        elif choice == '4':
            terminate_instance(instance_ids)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
