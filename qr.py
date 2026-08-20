import qrcode


# Ask the user for a website link.
wname = input("Enter a website name: ").strip()
website_link = input("Enter a website link: ").strip()

if not website_link.startswith(("http://", "https://")):
	print("Please enter a valid link starting with http:// or https://")
else:
	# Create the QR code and save it as an image.
	qr_code = qrcode.make(website_link)
	file_name = wname + ".png"
	qr_code.save(file_name)
	print(f"QR code saved as {file_name}")
	print("\n===== QR CODE GENERATOR =====")
	print("1. Website link")
	print("2. Plain text")
	print("3. Phone number")
	print("4. Social media handle")
	print("5. Wi-Fi details")
	print("6. Document or image link/path")
	print("7. Email address")


	if choice == "1":
		return input("Enter the website link: ").strip()

	if choice == "2":
		return input("Enter the text: ").strip()

	if choice == "3":
		phone = input("Enter the phone number: ").strip()
		return "tel:" + phone

	if choice == "4":
		platform = input("Enter the platform name: ").strip()
		handle = input("Enter the handle: ").strip()
		return "Social media: " + platform + " - " + handle

	if choice == "5":
		wifi_name = input("Enter the Wi-Fi name: ").strip()
		wifi_password = input("Enter the Wi-Fi password: ").strip()
		security = input("Enter security type (WPA, WEP, or nopass): ").strip()
		return "WIFI:T:" + security + ";S:" + wifi_name + ";P:" + wifi_password + ";;"

	if choice == "6":
		print("Use a shareable link for another person to open the file.")
		file_location = input("Enter the document/image link or file path: ").strip()
		return file_location

	if choice == "7":
		email = input("Enter the email address: ").strip()
		return "mailto:" + email

	return ""


selected_option = input("Choose an option (1-7): ").strip()
qr_data = get_qr_data(selected_option)

if qr_data == "":
	print("Please choose a valid option and enter some data.")
else:
	file_name = input("Enter a name for the QR image: ").strip()
	if file_name == "":
		file_name = "my_qr_code"

	qr_code = qrcode.make(qr_data)
	qr_code.save(file_name + ".png")
	print("QR code saved as " + file_name + ".png")
