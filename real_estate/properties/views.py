from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import InquiryForm
from .models import Category, Property

def home(request):
    return render(request, "home.html", {
        "properties": Property.objects.all()[:5],
        "categories": Category.objects.all(),
    })

def about(request):
    return render(request, "about.html")

def property_list(request):
    properties = Property.objects.all()
    query = request.GET.get("q", "").strip()
    if query:
        properties = properties.filter(title__icontains=query) | properties.filter(location__icontains=query)
    return render(request, "properties.html", {
        "properties": properties,
        "categories": Category.objects.all(),
        "query": query,
    })

def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.property = property_obj
            inquiry.save()
            messages.success(request, "Thank you! Your inquiry has been submitted successfully. Our team will contact you shortly.")
            return redirect("property_detail", pk=property_obj.pk)
    else:
        form = InquiryForm()
    return render(request, "property_detail.html", {"property": property_obj, "form": form})

def contact(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            property_id = request.POST.get("property")
            inquiry.property = Property.objects.filter(pk=property_id).first() if property_id else Property.objects.first()
            if inquiry.property:
                inquiry.save()
                messages.success(request, "Thank you for contacting Prime Homes. We will get back to you shortly.")
                return redirect("contact")
    else:
        form = InquiryForm()
    return render(request, "contact.html", {"form": form, "properties": Property.objects.all()})
