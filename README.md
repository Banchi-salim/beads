# BeadsByUmukulthum - Django E-Commerce Store

A complete Django-based e-commerce application for selling handcrafted bead jewelry with Paystack payment integration.

## Setup Complete! ✅

The project has been fully restructured and is ready to use.

## Quick Start

### 1. Server is Already Running
Visit: **http://127.0.0.1:8000/**

### 2. Create Admin Account
To access the admin panel and manage products, create a superuser:
```bash
python manage.py createsuperuser
```

Then access the admin panel at: **http://127.0.0.1:8000/admin/**

### 3. Add Product Images

#### Option A: Through Admin Panel (Recommended)
1. Go to http://127.0.0.1:8000/admin/
2. Click on "Products"
3. Select a product
4. Upload an image in the "Image" field
5. Click "Save"

#### Option B: Copy Existing Images
If you have product images in a folder:
```bash
# Create the media directory if it doesn't exist
mkdir -p media/products

# Copy your images to the media folder
# Example: copy Images/*.jpeg media/products/
```

Then update products in the admin panel to link to these images.

## Features

### User Features
- ✅ User Registration & Login
- ✅ User Profile with Order History
- ✅ Shopping Cart (Session-based)
- ✅ Product Browsing by Category
- ✅ Checkout with Delivery Information
- ✅ Paystack Payment Integration
- ✅ Order Confirmation & Success Page

### Admin Features
- ✅ Product Management
- ✅ Category Management
- ✅ Order Management
- ✅ User Management
- ✅ Easy Image Upload

## Database

**Current Products in Database: 9**
- 3 Necklaces
- 3 Earrings
- 3 Bracelets

All products have been pre-loaded from your original HTML file.

## Configure Paystack (Important!)

To enable payment processing:

1. Get your API keys from: https://dashboard.paystack.com/#/settings/developer
2. Open `beads_store/settings.py`
3. Update lines 148-149 with your actual keys:
```python
PAYSTACK_PUBLIC_KEY = 'pk_test_your_actual_key_here'
PAYSTACK_SECRET_KEY = 'sk_test_your_actual_key_here'
```

## Available URLs

- **Homepage**: http://127.0.0.1:8000/
- **Shop/Products**: http://127.0.0.1:8000/shop/
- **Login**: http://127.0.0.1:8000/accounts/login/
- **Sign Up**: http://127.0.0.1:8000/accounts/signup/
- **Profile**: http://127.0.0.1:8000/accounts/profile/
- **Shopping Cart**: http://127.0.0.1:8000/cart/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Project Structure

```
beads/
├── accounts/          # User authentication and profiles
├── cart/              # Shopping cart functionality
├── orders/            # Order processing and Paystack integration
├── products/          # Product and category management
├── static/            # CSS, JavaScript, images
│   └── css/
│       └── style.css  # Your original styles preserved
├── templates/         # HTML templates
│   └── base.html      # Base template with navigation
├── media/             # User-uploaded content (product images)
└── beads_store/       # Project settings
    └── settings.py    # Configuration file
```

## Managing Products

### Add New Products
1. Login to admin panel
2. Go to Products → Add Product
3. Fill in:
   - Name
   - Category (Necklaces, Earrings, or Bracelets)
   - Description
   - Price (in Naira)
   - Stock quantity
   - Upload image
   - Check "Available" checkbox
4. Save

### Edit Existing Products
1. Go to Products in admin
2. Click on product name
3. Make changes
4. Save

## Testing the Complete Flow

1. **Browse Products**: Go to homepage or shop page
2. **Add to Cart**: Click "Add to Cart" on any product
3. **View Cart**: Click the cart icon in navigation
4. **Checkout**: Click "Proceed to Checkout"
5. **Fill Details**: Enter delivery information
6. **Pay**: Click "Place Order & Pay with Paystack" (requires valid Paystack keys)
7. **Confirmation**: View order success page

## Next Steps

1. ✅ Create superuser account: `python manage.py createsuperuser`
2. ✅ Add product images through admin panel
3. ✅ Add your Paystack API keys in settings.py
4. ✅ Test the complete shopping flow
5. ✅ Customize as needed!

## Technical Details

- **Framework**: Django 5.2.9
- **Database**: SQLite (default, can be changed to PostgreSQL for production)
- **Payment Gateway**: Paystack
- **Image Handling**: Pillow
- **Session Storage**: Cart items stored in sessions

## Support

For Paystack integration help: https://paystack.com/docs/
For Django documentation: https://docs.djangoproject.com/

---

**Built for BeadsByUmukulthum** - Handcrafted jewelry with passion and precision
