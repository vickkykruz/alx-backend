function createPushNotificationsJobs(jobs, queue) {
  // Check if the jobs passed is an array
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');

  // Loop each job
  jobs.forEach((job) => {
    // Create a queue for each job
    const newJob = queue.create('push_notification_code_3', job).save((err) => {
      if (!err) console.log(`Notification job created: ${newJob.id}`);
    });

    // Indicate the following process
    newJob.on('complete', () => {
      console.log(`Notification job ${newJob.id} completed`);
    });
    newJob.on('failed', (err) => {
      console.log(`Notification job ${newJob.id} failed: ${err}`);
    });
    newJob.on('progress', (progress) => {
      console.log(`Notification job ${newJob.id} ${progress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
