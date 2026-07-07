using UnityEngine;

public class TargetSelector : MonoBehaviour
{
    public RosCommunication rosBridge;

    public void OnObjectSelected()
    {
        if (rosBridge != null)
        {
            rosBridge.SendPositionToRos(tronsform.position);
        }
        else 
        {
            Debug.LogError("ROS bridge not found");
        }
    }
}