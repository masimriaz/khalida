# Course Registration Setup Guide

## 🎯 Registration Form Implementation

Your registration form is now created at `register.html` and collects:

- First Name
- Last Name
- Email Address
- Phone Number
- Course Name (dropdown selection)
- Comments/Questions
- Registration Date (automatic)

---

## 📊 **RECOMMENDED: Google Forms Solution (Easiest)**

### Why Google Forms?

✅ **Free forever**
✅ **Automatic CSV export**
✅ **Built-in reporting & charts**
✅ **No coding required**
✅ **Email notifications**
✅ **Spam protection**

### Setup Steps:

1. **Create Google Form:**

   - Go to https://forms.google.com
   - Click "+ Blank Form"
   - Add these fields:
     - First Name (Short answer, Required)
     - Last Name (Short answer, Required)
     - Email (Short answer, Required)
     - Phone (Short answer, Required)
     - Course Name (Dropdown, Required) - Add all your courses
     - Comments (Paragraph, Optional)

2. **Configure Settings:**

   - Click Settings (gear icon)
   - ✓ Collect email addresses
   - ✓ Limit to 1 response (optional)
   - ✓ Edit after submit (optional)

3. **Get Embed Code:**

   - Click "Send" button
   - Click `< >` (embed icon)
   - Copy the iframe code
   - OR just use the form link directly

4. **View Responses:**

   - Click "Responses" tab
   - Click green Sheets icon to create spreadsheet
   - **Export CSV:** File → Download → CSV

5. **Update Your Website:**
   Replace the current form in `register.html` with a link or embed to your Google Form

---

## 📧 **ALTERNATIVE: FormSpree Solution (Current Implementation)**

### Setup Steps:

1. **Create FormSpree Account:**

   - Go to https://formspree.io
   - Sign up (free tier: 50 submissions/month)
   - Create a new form

2. **Get Your Form ID:**

   - Copy your form endpoint (looks like `xyzabc12`)

3. **Update register.html:**

   - Open `register.html`
   - Find line: `action="https://formspree.io/f/YOUR_FORM_ID"`
   - Replace `YOUR_FORM_ID` with your actual ID
   - Example: `action="https://formspree.io/f/xyzabc12"`

4. **View Submissions:**
   - Log into FormSpree dashboard
   - View all submissions
   - Export to CSV (available in paid plans)
   - Free tier: submissions sent to your email

### Pros:

- Submissions sent to your email
- Simple integration
- Spam filtering

### Cons:

- Limited free tier (50/month)
- CSV export requires paid plan
- Manual data compilation

---

## 🔧 **ADVANCED: Google Sheets API (Most Flexible)**

If you want data to go directly to Google Sheets from your custom form:

### Setup Steps:

1. **Create Google Sheet:**

   - Create new sheet with columns: First Name, Last Name, Email, Phone, Course Name, Comments, Registration Date

2. **Create Apps Script:**
   - Tools → Script Editor
   - Paste this code:

```javascript
function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSheet();
  var data = JSON.parse(e.postData.contents);

  sheet.appendRow([
    new Date(),
    data.firstName,
    data.lastName,
    data.email,
    data.phone,
    data.courseName,
    data.comments,
  ]);

  return ContentService.createTextOutput(
    JSON.stringify({ success: true })
  ).setMimeType(ContentService.MimeType.JSON);
}
```

3. **Deploy:**

   - Deploy → New deployment
   - Type: Web app
   - Execute as: Me
   - Who has access: Anyone
   - Copy the web app URL

4. **Update Form:**
   - Modify the form action to use your Apps Script URL
   - Update JavaScript to send data as JSON

---

## 🎨 Adding Registration Link to Main Website

Update `index.html` to add registration buttons:

### In Programs Section:

Add this button to each program card:

```html
<a href="register.html" class="btn btn-primary-custom btn-sm mt-3">
  <i class="fas fa-user-plus me-2"></i>Register Now
</a>
```

### In Navigation:

Add to navbar in `index.html`:

```html
<li class="nav-item">
  <a class="nav-link" href="register.html">Register</a>
</li>
```

### In Hero Section:

Add as a CTA button:

```html
<a class="btn btn-primary-custom btn-lg" href="register.html">
  Register for Courses
</a>
```

---

## 📈 Viewing Reports

### Google Forms Method:

1. Open your Google Form
2. Click "Responses" tab
3. View summary charts automatically
4. Click Sheets icon for detailed data
5. Create pivot tables, charts, filters

### FormSpree Method:

1. Login to FormSpree dashboard
2. View submissions list
3. Export data (paid plans)
4. Compile in Excel/Sheets manually

---

## 🚀 **RECOMMENDED NEXT STEPS:**

1. ✅ **Use Google Forms** (simplest, best for non-technical setup)

   - Takes 10 minutes to set up
   - Free forever
   - Built-in reporting
   - Easy CSV export

2. **OR** Set up FormSpree if you want to keep the custom design

   - Update `YOUR_FORM_ID` in register.html
   - Test the form
   - Check email for submissions

3. **Add registration links** to your main website

---

## 📝 Test Your Form

Before going live:

1. Submit a test registration
2. Verify you receive the data
3. Check CSV export works
4. Test on mobile devices

---

## 🆘 Need Help?

- Google Forms Tutorial: https://support.google.com/docs/answer/6281888
- FormSpree Docs: https://help.formspree.io/
- Apps Script Guide: https://developers.google.com/apps-script

Choose the method that works best for you! **Google Forms is recommended for easiest setup.**
