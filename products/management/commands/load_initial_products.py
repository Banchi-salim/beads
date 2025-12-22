from django.core.management.base import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):
    help = 'Load initial product data from the original beads.html'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating categories...')

        # Create categories
        necklaces, _ = Category.objects.get_or_create(
            name='Necklaces',
            defaults={'description': 'Beautiful handcrafted necklaces'}
        )
        earrings, _ = Category.objects.get_or_create(
            name='Earrings',
            defaults={'description': 'Elegant earrings for every occasion'}
        )
        bracelets, _ = Category.objects.get_or_create(
            name='Bracelets',
            defaults={'description': 'Stylish bracelets that tell your story'}
        )

        self.stdout.write(self.style.SUCCESS('Categories created!'))
        self.stdout.write('Creating products...')

        # Necklaces
        products_data = [
            # Necklaces
            {
                'category': necklaces,
                'name': 'Sunset Dream Necklace',
                'description': 'Handcrafted with glass yellow and black beads colors.',
                'price': 3000,
                'stock': 10,
            },
            {
                'category': necklaces,
                'name': 'Forest Spirit Necklace',
                'description': 'Green and white beads with crystal accents. Nature-inspired design.',
                'price': 2000,
                'stock': 10,
            },
            {
                'category': necklaces,
                'name': 'Royal Elegance Necklace',
                'description': 'Intricate beadwork with gold and silver accents. Perfect for special occasions.',
                'price': 4000,
                'stock': 10,
            },

            # Earrings
            {
                'category': earrings,
                'name': 'Glass Beaded Earrings',
                'description': 'Elegant crystal clear and blue bead drops with intricate patterns. Lightweight and stylish.',
                'price': 3000,
                'stock': 15,
            },
            {
                'category': earrings,
                'name': 'Small Hoop Earrings',
                'description': 'Elegant blue bead hoops with intricate detailing. Perfect for special occasions.',
                'price': 3000,
                'stock': 15,
            },
            {
                'category': earrings,
                'name': 'Blueberry Earrings',
                'description': 'Beautiful blue bead studs with silver backing. Comfortable for all-day wear.',
                'price': 2000,
                'stock': 20,
            },

            # Bracelets
            {
                'category': bracelets,
                'name': 'Blossom Glow Bracelet',
                'description': 'A touch of elegance. Adjustable closure.',
                'price': 4000,
                'stock': 12,
            },
            {
                'category': bracelets,
                'name': 'Rainbow Friendship Bracelet',
                'description': 'Colorful bracelet with a meaningful pattern. Perfect gift for friends.',
                'price': 2000,
                'stock': 18,
            },
            {
                'category': bracelets,
                'name': 'Flower Beaded Bracelet',
                'description': 'Delicate bracelet with colorful flower and intricate beadwork.',
                'price': 3000,
                'stock': 15,
            },
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Already exists: {product.name}'))

        self.stdout.write(self.style.SUCCESS('All products loaded successfully!'))
        self.stdout.write(f'Total products in database: {Product.objects.count()}')
