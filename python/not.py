#!/usr/bin/python
import sys
import pynotify
import sys


if len(sys.argv) == 3:
	title = sys.argv[1]
	message = sys.argv[2]

	if __name__ == "__main__":
	    if not pynotify.init("icon-summary-body"):
	        sys.exit(1)

	    n = pynotify.Notification(title,message,"notification-message-im")
	    n.show()

