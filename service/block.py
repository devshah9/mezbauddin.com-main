from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class ServiceCardBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=True, max_length=100)
    description = blocks.TextBlock(required=True)

    class Meta:
        icon = 'image'
        label = 'Service Card'
        template = 'staging/service_card_block.html'
