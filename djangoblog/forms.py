from django import forms
from .models import BlogPost



class BlogPostModelForm(forms.ModelForm):
    
    class Meta :
        model =  BlogPost
        fields = ['title','slug','image','content','publish_date']
        
    def cleaned_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs =qs.exclude(pk=instance.pk)#Removes the actual instance itself
        if qs.exists():
            raise forms.ValidationError("Title Already exists")
        return title