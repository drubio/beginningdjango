from coffeehouse.about.forms import ContactForm


class ContactCommentOnlyForm(ContactForm):
    def __init__(self, *args, **kwargs):
        super(ContactCommentOnlyForm, self).__init__(*args, **kwargs)
        del self.fields['name']
        del self.fields['email']
        del self.fields['gender']
