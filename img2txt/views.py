from django.shortcuts import render
from django.http import HttpResponse
from django.forms import formset_factory
from django.views import View
from PIL import Image
import pytesseract
from .forms import ImageForm


# Read an image and extract text from it
def image_to_text(image, language):
    img = Image.open(image)
    text = pytesseract.image_to_string(img, lang=language) 
    return text


def index(request):
    # render index page
    return render(request, 'img2txt/index.html')


class ExtractText(View):
    template = 'img2txt/extract_text.html'
    ImageFormSet = formset_factory(ImageForm, extra=2)
    texts = []

    def post(self, request):
        formset = self.ImageFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # extract texts from each form in image_formset and append it to self.text
            for form in formset:
                image = form.cleaned_data['image']
                language = form.cleaned_data['language']
                text = image_to_text(image, language)
                self.texts.append(text)
                context = {'formset': self.ImageFormSet(), 'texts': self.texts}
            return render(request, self.template, context)
        else:
            context = {'formset': formset}
            return render(request, self.template, context)

    def get(self, request):
        context = {'formset': self.ImageFormSet()}
        return render(request, self.template, context)


