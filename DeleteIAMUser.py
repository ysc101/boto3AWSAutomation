import boto3

# Initialize IAM client
iam = boto3.client('iam')

# Specify the username to delete
username = 'testuser'  # Replace with the username to delete

try:
    # Detach all managed policies from the user
    attached_policies = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
    for policy in attached_policies:
        iam.detach_user_policy(UserName=username, PolicyArn=policy['PolicyArn'])
        print(f"Detached policy: {policy['PolicyName']}")

    # Remove the user from all groups
    groups = iam.list_groups_for_user(UserName=username)['Groups']
    for group in groups:
        iam.remove_user_from_group(UserName=username, GroupName=group['GroupName'])
        print(f"Removed user from group: {group['GroupName']}")

    # Delete all inline policies
    inline_policies = iam.list_user_policies(UserName=username)['PolicyNames']
    for policy_name in inline_policies:
        iam.delete_user_policy(UserName=username, PolicyName=policy_name)
        print(f"Deleted inline policy: {policy_name}")

    # Delete access keys
    access_keys = iam.list_access_keys(UserName=username)['AccessKeyMetadata']
    for access_key in access_keys:
        iam.delete_access_key(UserName=username, AccessKeyId=access_key['AccessKeyId'])
        print(f"Deleted access key: {access_key['AccessKeyId']}")

    # Finally, delete the user
    iam.delete_user(UserName=username)
    print(f"User '{username}' has been deleted successfully.")

except Exception as e:
    print(f"Error deleting user: {e}")
