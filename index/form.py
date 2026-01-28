from django import forms


class StateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        player_choices = kwargs.pop('player_choices', [])
        role_choices = kwargs.pop('role_choices', [])
        super().__init__(*args, **kwargs)
        self.fields['player'].choices = player_choices
        self.fields['role'].choices = role_choices

    player = forms.ChoiceField(label='Player', widget=forms.Select(attrs={'id':'playertags'}))
    role = forms.ChoiceField(label='Role', widget=forms.Select(attrs={'id':'roletags'}))


class TeamForm(forms.Form):
    one = forms.CharField(label='Team 1', max_length=100, widget=forms.TextInput(attrs={'class':'teamtags'}))
    two = forms.CharField(label='Team 2', max_length=100, widget=forms.TextInput(attrs={'class':'teamtags'}))
    type = forms.CharField(label='Type', max_length=100, widget=forms.TextInput(attrs={'class':'typetags'}))


class OneBatsmanForm(forms.Form):
    one_batsman_one = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_batsman_two = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_batsman_three = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_batsman_four = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_batsman_five = forms.CharField(required = False, label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_batsman_six = forms.CharField(required = False, label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))


class OneBowlerForm(forms.Form):
    one_bowler_one = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_bowler_two = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_bowler_three = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_bowler_four = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_bowler_five = forms.CharField(required = False, label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_bowler_six = forms.CharField(required = False, label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))


class OneAllrounderForm(forms.Form):
    one_allrounder_one = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_allrounder_two = forms.CharField(required = False, label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_allrounder_three = forms.CharField(required = False, label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))
    one_allrounder_four = forms.CharField(required = False, label='', max_length=100, widget=forms.TextInput(attrs={'class':'oneplayertags'}))


class TwoBatsmanForm(forms.Form):
    two_batsman_one = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_batsman_two = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_batsman_three = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_batsman_four = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_batsman_five = forms.CharField(required=False, label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_batsman_six = forms.CharField(required=False, label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))

class TwoBowlerForm(forms.Form):
    two_bowler_one = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_bowler_two = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_bowler_three = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_bowler_four = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_bowler_five = forms.CharField(required=False, label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_bowler_six = forms.CharField(required=False, label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))

class TwoAllrounderForm(forms.Form):
    two_allrounder_one = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_allrounder_two = forms.CharField(required=False, label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_allrounder_three = forms.CharField(required=False, label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))
    two_allrounder_four = forms.CharField(required=False, label='', max_length=100, widget=forms.TextInput(attrs={'class': 'twoplayertags'}))