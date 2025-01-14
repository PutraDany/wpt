def main(request, response):
  if request.cookies.get(b"cookie") != b"1":
    return (530, [], "Missing cookie")
  if request.method != "POST":
    return (531, [], "Method is not POST")
  if request.headers.get(b"Content-Type") != b"application/x-www-form-urlencoded":
    return (532, [], "Wrong Content-Type")
  if request.headers.get(b"Accept") != b"application/json":
    return (533, [], "Wrong Accept")
  if request.headers.get(b"Sec-Fetch-Dest") != b"webidentity":
    return (500, [], "Wrong Sec-Fetch-Dest header")
  if request.headers.get(b"Referer"):
    return (534, [], "Should not have Referer")
  if not request.headers.get(b"Origin"):
    return (535, [], "Missing Origin")
  if request.headers.get(b"Sec-Fetch-Mode") != b"no-cors":
    return (539, [], "Wrong Sec-Fetch-Mode header")
  if request.headers.get(b"Sec-Fetch-Site") != b"none":
    return (540, [], "Wrong Sec-Fetch-Site header")

  if not request.POST.get(b"client_id"):
    return (536, [], "Missing 'client_id' POST parameter")
  if not request.POST.get(b"account_id"):
    return (537, [], "Missing 'account_id' POST parameter")
  if not request.POST.get(b"disclosure_text_shown"):
    return (538, [], "Missing 'disclosure_text_shown' POST parameter")
  if not request.POST.get(b"is_account_auto_selected"):
    return (541, [], "Missing 'is_account_auto_selected' POST parameter")

  response.headers.set(b"Content-Type", b"application/json")

  return "{\"token\": \"token\"}"
