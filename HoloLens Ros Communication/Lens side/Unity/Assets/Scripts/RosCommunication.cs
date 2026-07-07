using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using RosMessageTypes.Std;
using RosMessageTypes.Geometry;

public class RosCommunication : MonoBehaviour
{
    private ROSConnection ros;
    public string importedTopicName = "ros_to_unity_topic";
    public string exportedTopicName = "unity_to_ros_topic";
    void Start()
    {
        ros = ROSConnection.GetOrCreateInstance();
        ros.Subscribe<StringMsg>(importedTopicName, OnHeartbeatReceived);
        ros.RegisterPublisher<PointMsg>(exportedTopicName);
        Debug.Log($"Bridge Initialized. Listening on '{importedTopicName}' and publishing on '{exportedTopicName}'");
    }


    public void SendPositionToRos()
    {
        if (ros == null)
        {
            Debug.LogWarning("ROS connection not ready yet.");
            return;
        }

        Vector3 currentPosition = transform.position;
        PointMsg positionMessage = new PointMsg(
            currentPosition.x,
            currentPosition.y,
            currentPosition.z
        );
        ros.Publish(exportedTopicName, positionMessage);
        Debug.Log($"Sent coordinates to ROS: X={currentPosition.x}, Y={currentPosition.y}, Z={currentPosition.z}");
    }

    public void SendPositionToRos(Vector3 targetPosition)
    {
        if (ros == null)
        {
            Debug.LogWarning("ROS connection not ready yet.");
            return;
        }

        PointMsg positionMessage = new PointMsg(
            targetPosition.x,
            targetPosition.y,
            targetPosition.z
        );
        
        ros.Publish(exportedTopicName, positionMessage);
        Debug.Log($"Sent selected coordinates to ROS: X={targetPosition.x}, Y={targetPosition.y}, Z={targetPosition.z}");
    }   

    private void OnHeartbeatReceived(StringMsg msg)
    {
        Debug.Log($"received from Server: {msg.data}");
    }
}