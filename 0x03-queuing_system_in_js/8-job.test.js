import createPushNotificationsJobs from './8-job';
import { expect } from 'chai';
import sinon from 'sinon';
import kue from 'kue';


const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    sinon.spy(console, 'log');
  });

  afterEach(() => {
    sinon.restore();
  });

  queue.testMode.enter();

  it('display a error message if jobs is not an array', () => {
    createPushNotificationsJobs('jobs', queue);
    expect(console.log.calledOnceWith('Jobs is not an array')).to.be.true;
  });

  it('create two new jobs to the queue', () => {
    const list = [
      {
        phoneNumber: '1234567890',
        message: 'Hello',
      },
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(1);
  });

  it('create two new jobs to the queue', () => {
    const list = [
      {
        phoneNumber: '1234567890',
        message: 'Hello',
      },
      {
        phoneNumber: '0987654321',
        message: 'World',
      },
    ];
    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(list[0]);
  });

  it('call console.log with the right message on failed', () => {
    const list = [
      {
        phoneNumber: '1234567890',
        message: 'Hello',
      },
    ];
    createPushNotificationsJobs(list, queue);
    queue.testMode.jobs[0].emit('failed');
    expect(
      console.log.calledWith(
        `Notification job ${queue.testMode.jobs[0].id} failed: undefined`
      )
    ).to.be.true;
  });

  it('call createPushNotificationsJobs', () => {
    const list = [
      {
        phoneNumber: '1234567890',
        message: 'Hello',
      },
    ];
    const spy = sinon.spy(createPushNotificationsJobs);
    spy(list, queue);
    expect(spy.calledOnceWithExactly(list, queue)).to.be.true;
  });

  queue.testMode.exit();
});
