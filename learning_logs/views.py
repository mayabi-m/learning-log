from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')
def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}    
    return render(request, 'learning_logs/topics.html', context)
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}  
    return render(request, 'learning_logs/topic.html', context)
def new_topic(request):
    """Add a new topic."""
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    else:
        form = TopicForm()
    context = {'form': form}    

    return render(request, 'learning_logs/new_topic.html', context)
def new_entry(request, topic_id): 
    """Add a new entry for a topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    else:
        form = EntryForm()
    context = {'topic': topic, 'form': form}    
    return render(request, 'learning_logs/new_entry.html', context)
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    else:
        form = EntryForm(instance=entry)
    context = {'entry': entry, 'topic': topic, 'form': form}    
    return render(request, 'learning_logs/edit_entry.html', context)