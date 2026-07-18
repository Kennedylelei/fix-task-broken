There is an Apache-style access log at /app/access.log. Parse it and write a JSON
summary report to /app/report.json with exactly these keys:

1. "total_requests" — the total number of log lines (integer).
2. "unique_ips" — the number of distinct client IP addresses (integer).
3. "top_path" — the request path (e.g. "/index.html") requested most often
   across all lines (string). The input has no tie for the top path.

Do not modify /app/access.log.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.