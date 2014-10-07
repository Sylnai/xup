import codecs, sys, datetime, logging
from filetail import FileTail
if __name__ == "__main__":
    log = logging.getLogger(__name__)
    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    out_hdlr.setLevel(logging.INFO)
    log.addHandler(out_hdlr)
    log.setLevel(logging.INFO)

    tail = FileTail(sys.argv[1])

    count = 0
    time = None
    log.info("Initiated xcounter on %s" % sys.argv[1])
    for line in tail:
        line = line.rstrip("\r\n")
        if line.count(" -"):
            log.info("Count from %s is %d" % (str(time), count))
            time = datetime.datetime.now()
            count = 0
        elif line.count(" x"):
            count += 1
            log.info(str(count))
