# EC2 Management Script

This Python script provides a basic interface to manage Amazon EC2 instances. Using the `boto3` library, you can start, stop, reboot, or terminate EC2 instances by their IDs.

## Features

- **Start Instances**: Starts specified EC2 instances.
- **Stop Instances**: Stops specified EC2 instances.
- **Reboot Instances**: Reboots specified EC2 instances.
- **Terminate Instances**: Terminates specified EC2 instances.

## Prerequisites

- Python 3.x
- `boto3` library
- AWS credentials configured with appropriate permissions

## Setup

1. **Install Dependencies**

   Install the `boto3` library using pip:

   ```bash
   pip install boto3
   ```

2. **Configure AWS Credentials**

   Ensure that your AWS credentials are configured. You can do this using the AWS CLI:

   ```bash
   aws configure
   ```

   Provide your AWS Access Key ID, Secret Access Key, default region name, and output format when prompted.

## Usage

1. **Run the Script**

   Execute the script using Python:

   ```bash
   python index.py
   ```

2. **Choose an Action**

   When prompted, choose an action by entering the corresponding number:

   - **1**: Start Instances
   - **2**: Stop Instances
   - **3**: Reboot Instances
   - **4**: Terminate Instances
   - **5**: Exit

   Enter instance IDs separated by commas when prompted.

## Example

```text
Choose an action:
1. Start Instances
2. Stop Instances
3. Reboot Instances
4. Terminate Instances
5. Exit
Enter choice: 2
Enter instance IDs separated by commas: i-1234567890abcdef0,i-0abcdef1234567890
```

This will stop the specified EC2 instances.

## Error Handling

The script includes basic error handling for issues like invalid instance IDs or network problems. Error messages will be displayed if any issues occur during the execution.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

