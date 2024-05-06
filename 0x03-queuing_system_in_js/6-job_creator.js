import kue from 'kue';

const queue = kue.createQueue();
const jobData = {
  phoneNumber: '155986848',
  message: '£ This is to verify your account',
};

const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed', (err) => {
    console.log('Notification job failed');
  });
