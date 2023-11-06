import os

def check_existing_ros2_container(name):
    """
    Check for an existing Docker container named 'ros2' using bash commands.
    """
    command = f'docker ps -a --format "{{{{.Names}}}}" | grep -w "{name}"'
    result = os.system(command)
    return result == 0

def build_and_create_container(name):
    """
    Build a Docker image from a Dockerfile and create a new Docker container using bash commands.
    """
    if check_existing_ros2_container(name):
        print(f"A 'ros2' container already exists. Skipping container creation.")
    else:
        dockerfile_dir = os.path.abspath(os.path.join(os.getcwd(), "docker"))
        image_name = name
        build_context = os.getcwd()

        try:
            # Use bash commands to build the Docker image from the Dockerfile with the correct build context
            os.system(f'docker build -t {image_name} -f {dockerfile_dir}/Dockerfile {build_context}')

            # Use bash commands to create and run the container
            os.system(f'docker run -d --name {name} {image_name}')
            print(f"Container {name} has been started.")
        except Exception as e:
            print(f"Failed to build or create the Docker container: {e}")

def main():
    build_and_create_container("ros2")

if __name__ == "__main__":
    main()
