from setuptools import find_packages, setup

package_name = 'unity_robot_comm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Elyes',
    maintainer_email='elyes298@github.com',
    description='ROS 2 to Unity Communication Test Package',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'unity_communicator = unity_robot_comm.communication_node:main',
        ],
    },
)
