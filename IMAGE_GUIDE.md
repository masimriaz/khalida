# Image Assets Guide

## Required Images for Khalida Foundation Website

This document lists all images needed for the website to display properly.

### 📁 Directory Structure

```
assets/
└── img/
    ├── bg-masthead.jpg          (Hero background)
    ├── ai-poster-1.jpg          (AI program poster)
    ├── course-outline.jpg       (Course curriculum)
    ├── gallery-1.jpg            (Scholarship event)
    ├── gallery-2.jpg            (Classroom)
    ├── gallery-3.jpg            (Teacher training)
    ├── gallery-4.jpg            (Community event)
    └── gallery-5.jpg            (Skills workshop)
```

### 🎯 Image Specifications

| Image File           | Purpose                 | Recommended Size | Format  | Notes                                   |
| -------------------- | ----------------------- | ---------------- | ------- | --------------------------------------- |
| `bg-masthead.jpg`    | Hero section background | 1920x1080px      | JPG     | High quality, inspiring education image |
| `ai-poster-1.jpg`    | AI program showcase     | 800x1000px       | JPG/PNG | Your AI course promotional poster       |
| `course-outline.jpg` | Curriculum details      | 1200x800px       | JPG/PNG | Course structure visual                 |
| `gallery-1.jpg`      | Scholarship ceremony    | 800x600px        | JPG     | Students receiving awards               |
| `gallery-2.jpg`      | Infrastructure          | 800x600px        | JPG     | Classroom/building                      |
| `gallery-3.jpg`      | Teacher training        | 800x600px        | JPG     | Workshop/training session               |
| `gallery-4.jpg`      | Community engagement    | 800x600px        | JPG     | Community event                         |
| `gallery-5.jpg`      | Skills workshop         | 800x600px        | JPG     | Hands-on learning                       |

### 🎨 Image Guidelines

**Style:**

- Professional and warm
- Natural lighting preferred
- Clear focus on subjects
- Authentic moments (not overly staged)

**Content:**

- Show diverse students and teachers
- Capture genuine learning moments
- Display your programs in action
- Include your AI program materials

**Technical:**

- High resolution (at least 72 DPI for web)
- Landscape orientation for most images
- Good color balance and contrast
- Minimal compression (preserve quality)

### 🔧 How to Add Your Images

#### Option 1: Replace Files Directly

1. Navigate to `assets/img/` folder
2. Add your images with the exact filenames listed above
3. Ensure file extensions match (.jpg or .png)

#### Option 2: Use Your Own Filenames

1. Add your images to `assets/img/` folder
2. Open `index.html`
3. Search for the old filename (e.g., "bg-masthead.jpg")
4. Replace with your filename (e.g., "hero-background.jpg")

### 📷 Free Stock Photo Resources

If you need temporary placeholder images:

**Education-themed photos:**

- Unsplash: https://unsplash.com/s/photos/education
- Pexels: https://www.pexels.com/search/students/
- Pixabay: https://pixabay.com/images/search/classroom/

**Search terms to use:**

- "students learning"
- "classroom education"
- "children studying"
- "teacher training"
- "school building"
- "community learning"
- "technology education"

**Important:** Use license-free images or ensure you have rights to use them!

### 🛠️ Image Optimization

Before uploading images to your website:

**Online Tools (Free):**

1. **TinyPNG** - https://tinypng.com

   - Compress JPG and PNG files
   - Reduces file size by 50-70%
   - Maintains visual quality

2. **Squoosh** - https://squoosh.app

   - Advanced compression options
   - Compare before/after
   - Convert to WebP format

3. **ImageOptim** (Mac) - https://imageoptim.com
   - Drag and drop optimization
   - Batch processing

**Desktop Software:**

- Adobe Photoshop (Export for Web)
- GIMP (free Photoshop alternative)
- XnConvert (free batch converter)

### ✅ Image Checklist

Before considering your images "done":

- [ ] All required images are present in `assets/img/`
- [ ] Images are optimized (compressed)
- [ ] File sizes are reasonable (< 500KB each)
- [ ] Images display correctly on the website
- [ ] Images are clear and professional quality
- [ ] Images represent your actual programs (when possible)
- [ ] You have rights to use all images
- [ ] Images work on mobile devices
- [ ] Alt text is descriptive in HTML

### 🎭 Temporary Placeholders

If you don't have images yet, the website will show:

- Broken image icons ❌
- Alt text descriptions
- Gray/white spaces

**This is normal!** Add your images when ready.

To create simple colored placeholders:

1. Use https://placeholder.com/
2. Example: `https://via.placeholder.com/1920x1080/1a3a52/ffffff?text=Hero+Background`
3. Replace URLs in `index.html` temporarily

### 📊 Image Performance Tips

**For Best Performance:**

- Use WebP format (modern browsers)
- Enable lazy loading (uncomment in HTML)
- Use appropriate dimensions (don't upload 4000px images)
- Compress aggressively (aim for < 200KB per image)

**Lazy Loading (Add to img tags):**

```html
<img src="image.jpg" loading="lazy" alt="Description" />
```

### 🆘 Troubleshooting

**Image not showing?**

- Check file path is correct
- Verify filename matches exactly (case-sensitive)
- Check file extension (.jpg vs .jpeg vs .png)
- Clear browser cache (Ctrl+F5)

**Image looks blurry?**

- Upload higher resolution version
- Check original image quality
- Ensure proper dimensions

**Page loads slowly?**

- Compress images more
- Reduce file sizes
- Consider WebP format
- Enable lazy loading

---

## Quick Reference: Where Images Appear

| Image              | Section       | Line # in HTML |
| ------------------ | ------------- | -------------- |
| bg-masthead.jpg    | Hero Section  | ~24 (CSS)      |
| ai-poster-1.jpg    | AI Initiative | ~320           |
| course-outline.jpg | AI Initiative | ~390           |
| gallery-1.jpg      | Gallery       | ~480           |
| gallery-2.jpg      | Gallery       | ~490           |
| gallery-3.jpg      | Gallery       | ~500           |
| gallery-4.jpg      | Gallery       | ~510           |
| gallery-5.jpg      | Gallery       | ~520           |

---

**Need help with images? Contact your web developer or designer!**
