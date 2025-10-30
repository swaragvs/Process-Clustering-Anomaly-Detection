# Assuming your original DataFrame is 'df'
# Group by the timestamp
df_time_series = df.groupby('timestamp').agg(
    total_cpu_percent=('cpu_percent', 'sum'),
    total_memory_percent=('memory_percent', 'sum'),
    total_disk_read_mb=('disk_read_mb', 'sum'),
    total_disk_write_mb=('disk_write_mb', 'sum'),
    # We only take the 'first' net value since they are all duplicates
    total_net_sent_mb=('net_sent_mb', 'first'), 
    total_net_recv_mb=('net_recv_mb', 'first')
).reset_index()

# Now, 'df_time_series' is the DataFrame you wanted all along.
# It has one row for each *second* and shows the *total system* usage.
print(df_time_series.head())

# --- Now, your time-series plot from Cell 5 will work! ---

# Convert timestamp to datetime
df_time_series['timestamp'] = pd.to_datetime(df_time_series['timestamp'], unit='s')

# Plot total CPU over time
plt.figure(figsize=(15, 5))
plt.plot(df_time_series['timestamp'], df_time_series['total_cpu_percent'])
plt.title('Total System CPU Usage Over Time')
plt.xlabel('Time')
plt.ylabel('Total CPU % (can be > 100)')
plt.show()