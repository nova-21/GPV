from add_collaborator import add_collaborator

try:
    repository_to_create = add_collaborator("Test9","nova-21")
    print(repository_to_create)
except ValueError as e:
    print(f"Error: {e}")