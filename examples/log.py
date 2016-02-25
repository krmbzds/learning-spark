errorLog = sc.textFile("logs/error_log")

errorInfo = errorLog.filter(lambda x: "info" in x)
errorNotice = errorLog.filter(lambda x: "notice" in x)
errorError = errorLog.filter(lambda x: "error" in x)

accessLog = sc.textFile("logs/access_log")

accessGet = accessLog.filter(lambda x: "GET" in x)
accessPost = accessLog.filter(lambda x: "POST" in x)
accessMail = accessLog.filter(lambda x: "mailman" in x)
accessWiki = accessLog.filter(lambda x: "twiki" in x)
