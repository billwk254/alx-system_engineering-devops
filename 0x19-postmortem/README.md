Postmortem Report: Web Service Outage
Issue Summary
Duration:
Start Time: 05/10/2023 22:30 (GMT +3)
End Time: 06/10/2023 04:20 (GMT +3)
Root Cause:
The root cause of the outage was identified as a misconfiguration in the load balancer settings. This misconfiguration resulted in improper distribution of incoming traffic among the available servers, leading to an overload on specific instances and subsequent service failure.
Timeline
Detection Time:
05/10/2023 22:37 (GMT +3) - The issue was first detected when monitoring systems triggered alerts for an unusual spike in server errors and a sharp decline in request success rates.
Issue Identification:
An engineer noticed a surge in customer complaints about service unavailability, confirming the ongoing issue.
Investigation Actions:
The investigation examined server logs, network configurations, and load balancer settings. Assumptions were initially focused on potential database issues and increased traffic due to a recent marketing campaign.
Misleading Paths:
Several misleading paths were explored, including database performance tuning and scaling up server capacity, delaying the identification of the misconfigured load balancer.
Escalation:
The incident was escalated to the infrastructure and networking teams as the investigation pointed towards a potential load-balancing issue. Collaborative efforts were initiated to expedite the resolution.
Resolution:
The root cause, a misconfiguration in the load balancer, was identified and corrected. Load balancing settings were adjusted to evenly distribute incoming traffic among servers, restoring normal service functionality.
Root Cause and Resolution
Root Cause:
The misconfiguration in the load balancer settings led to uneven distribution of traffic, causing some servers to handle a disproportionately high number of requests, ultimately leading to service degradation.
Resolution:
The issue was resolved by reconfiguring the load balancer settings to distribute incoming traffic among available servers evenly. Additionally, monitoring and alerting systems were enhanced to provide early detection of similar issues in the future.
Corrective and Preventative Measures
Improvements/Fixes:
Implement regular reviews of load balancer configurations to ensure proper distribution of incoming traffic.
Conduct comprehensive testing after any infrastructure changes to avoid service disruptions.
Enhance monitoring systems to provide real-time alerts for abnormal traffic patterns and server errors.
Tasks:
Conduct a thorough review of load balancer configurations.
Implement automated testing procedures for load balancer settings.
Enhance monitoring and alerting systems to detect similar issues promptly.
Conduct training sessions for the operations team to improve incident response times.
Document and share the lessons learned from this incident to improve team knowledge and awareness.
Conclusion
The web service outage was successfully resolved by identifying and correcting the misconfiguration in the load balancer settings.

THE LINK TO THE FULL POSTMOTERM REPORT IS BELOW HERE:

https://docs.google.com/document/d/1K0bMGkudfzKXbAvm_HNX9aD3aBtksGX4XFWMasMFqGM/edit?usp=sharing