if __name__=='__main__':

  request_queue = SetQueue(maxsize=-1)
  worker = Thread(target=request_queue.process_queue)
  worker.setDaemon(True)
  worker.start()


  while True:
    try:
      #Connect to the database get all the new requests to be verified
      db = Database(username_testschema, password_testschema, mother_host_testschema, mother_port_testschema, mother_sid_testschema, 0)
      #Get new requests for verification
      verify_these = db.query("SELECT JOB_ID FROM %s.table WHERE     JOB_STATUS='%s' ORDER BY JOB_ID" %
                             (username_testschema, 'INITIATED'))

      #If there are some requests to be verified, put them in the queue.
      if len(verify_these) > 0:
        for row in verify_these:
          print "verifying : %s" % row[0]
          verify_id = row[0]
          request_queue.put(verify_id)
    except Exception as e:
      logger.exception(e)
    finally:
      time.sleep(10)