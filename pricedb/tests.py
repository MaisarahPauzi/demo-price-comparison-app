from django.test import TestCase
from priceapi.views import parse_javascript_str
# Create your tests here.

class TestViewHelperFunctions(TestCase):
    def setUp(self):
        self.mockStrings = '''
       <script type="application/ld+json">[{"@context":"http://schema.org","@type":"WebSite","name":"Mudah.my - Malaysia's largest marketplace","alternateName":"Find all properties for sale in Malaysia on Mudah.my, Malaysia's largest marketplace. Happy Buying and Selling!","url":"https://www.mudah.my/penang/properties-for-sale-2000?q=Taman%20Pauh%20Indah%20Seberang%20Jaya"},{"@context":"http://schema.org","@type":"Organization","url":"https://www.mudah.my","logo":"https://lh5.googleusercontent.com/-bbFg-Sz79JM/AAAAAAAAAAI/AAAAA AAAQqQ/t1yVVVvftmU/s0-c-k-no-ns/photo.jpg","sameAs":["http://www.facebook.com/mudah.my","http://instagram.com/mudahmy","http://www.linkedin.com/company/mudah.my-sdn-bhd","http://plus.google.com/+Mudah","http://www.youtube.com/user/Mudahdotmy","https://twitter.com/mudah"]},{"@context":"http://schema.org","@type":"ItemList","url":"https://www.mudah.my/penang/properties-for-sale-2000?q=Taman%20Pauh%20Indah%20Seberang%20Jaya","numberOfItems":1,"itemListElement":[{"@type":"ListItem","position":"1","item":{"@type":"Product","url":"https://www.mudah.my/Double+Storey+Semi+D+Taman+Pauh+Indah+Seberang+Jaya+Penang-86368603.htm","name":"Double Storey Semi-D Taman Pauh Indah, Seberang Jaya, Penang","offers":{"@type":"Offer","priceCurrency":"MYR","price":"750000"},"category":"Houses","image":"https://img.rnudah.com/grids/56/563021106849177.jpg"}}]},{"@context":"http://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"item":{"@id":"https://www.mudah.my","name":"Home"}},{"@type":"ListItem","position":2,"item":{"@id":"https://www.mudah.my/penang","name":"Penang"}},{"@type":"ListItem","position":3,"item":{"@id":"https://www.mudah.my/penang/properties-for-sale-2000?q=Taman%20Pauh%20Indah%20Seberang%20Jaya","name":"Properties For Sale 2000?q=Taman Pauh Indah Seberang Jaya"}}]}]</script>
        '''
    
    def test_parse_javascript_function(self):
        returned_array = parse_javascript_str(self.mockStrings)
        for item_list in returned_array:
            self.assertEqual(item_list['item']['url'], 'https://www.mudah.my/Double+Storey+Semi+D+Taman+Pauh+Indah+Seberang+Jaya+Penang-86368603.htm')
            self.assertEqual(item_list['item']['name'], 'Double Storey Semi-D Taman Pauh Indah, Seberang Jaya, Penang')
            self.assertEqual(item_list['item']['image'], 'https://img.rnudah.com/grids/56/563021106849177.jpg')
            self.assertEqual(item_list['item']['offers']['price'], '750000')
