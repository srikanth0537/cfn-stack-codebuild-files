import sys
import boto3

def update_stack(stack_name):
    try:
        cf = boto3.client('cloudformation', region_name='ap-south-1')  # Replace with your AWS region
        cf.update_stack(
            StackName=stack_name,
            UsePreviousTemplate=True
        )
        print(f"Stack '{stack_name}' is updated successfully.")
    except cf.exceptions.ClientError as e:
        if "No updates are to be performed" in str(e):
            print(f"No changes to stack '{stack_name}' were detected.")
        else:
            print(f"An error occurred while updating stack '{stack_name}': {e}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python update_stack.py <stack_name1> <stack_name2> ...")
        sys.exit(1)

    stack_names = sys.argv[1:]  # Get stack names from command line arguments

    for stack_name in stack_names:
        update_stack(stack_name)
