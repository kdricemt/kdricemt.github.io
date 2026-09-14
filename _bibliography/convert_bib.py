from pybtex.database import parse_file
import yaml

def convert_bib_to_yaml_with_formatting_maganize(bib_file, yaml_file, highlight_author):
    # Parse the .bib file
    bib_data = parse_file(bib_file)

    publications = []
    bibtex_texts = {}
    
    for entry_key, entry in bib_data.entries.items():
        # Extracting fields
        fields = entry.fields

        # create a field except for pdf, video, code, id, and abstract
        field_bib = {}
        for key, value in fields.items():
            if key not in ['pdf', 'video', 'code', 'id', 'abstract', 'review', 'award', 'slides']:
                field_bib[key] = value

        authors = []
        authors_bib = []
        # Format authors in AIAA style: "Family name, Initials"
        for person in entry.persons.get('author', []):
            last_name = person.last_names[0]
            initials = ''.join([name[0].upper() + '.' for name in person.first_names + person.middle_names])
            full_name = f"{last_name}, {initials}"
            # full name for bibtex: write full name without initials
            full_name_bib = f"{last_name}, {' '.join(person.first_names + person.middle_names)}"
            authors_bib.append(full_name_bib)
            
            # Bold the specified author
            if highlight_author.lower() in ' '.join(person.first_names + person.last_names).lower():
                full_name = f"<strong>{full_name}</strong>"
                
            authors.append(full_name)

        # get the id number
        # ['id'] is C##NUMBER##, so we need to extract the number starting from the 2nd character
        fields['idnum'] = int(fields.get('id', 'C')[1:])

        # add authors to the field_bib
        field_bib['author'] = ' and '.join(authors_bib)

        # Generate the bibtex text
        bibtex_texts[id] = f" @{entry.type}{{{entry_key},\n" + \
                      '\n'.join([f"  {key} = {{{value}}}," for key, value in field_bib.items()]) + \
                      '\n}'

        
        # Construct the publication entry
        publication = {
            'id':  '[' + fields.get('id', '') + ']',
            'idnum': fields.get('idnum', ''),
            'volume': fields.get('volume', ''),
            'number': fields.get('number', ''),
            'pages': fields.get('pages', ''),
            'publisher': fields.get('publisher', ''),
            'url': fields.get('url', ''),
            'author': ', '.join(authors),
            'title': fields.get('title', ''),
            'journal': fields.get('journal', ''),
            'year': fields.get('year', ''),
            'year_num': int(fields.get('year', '')),
            'pdf': fields.get('pdf', ''),
            'video': fields.get('video', ''),         
            'code': fields.get('code', ''),
            'abstract': fields.get('abstract', ''),
            'bibtex': bibtex_texts[id],
            'review': fields.get('review', '')
        }
        
        publications.append(publication)

    # reorder the publications by id number (descending)
    publications = sorted(publications, key=lambda x: x['idnum'], reverse=True)

    # Write to YAML
    with open(yaml_file, 'w') as yaml_out:
        yaml.dump(publications, yaml_out, sort_keys=False, allow_unicode=True, default_flow_style=False)

def convert_bib_to_yaml_with_formatting_journal(bib_file, yaml_file, highlight_author):
    # Parse the .bib file
    bib_data = parse_file(bib_file)

    publications = []
    bibtex_texts = {}
    
    for entry_key, entry in bib_data.entries.items():
        # Extracting fields
        fields = entry.fields

        # create a field except for pdf, video, code, id, and abstract
        field_bib = {}
        for key, value in fields.items():
            if key not in ['pdf', 'video', 'code', 'id', 'abstract', 'review', 'award', 'slides']:
                field_bib[key] = value

        authors = []
        authors_bib = []
        # Format authors in AIAA style: "Family name, Initials"
        for person in entry.persons.get('author', []):
            last_name = person.last_names[0]
            initials = ''.join([name[0].upper() + '.' for name in person.first_names + person.middle_names])
            full_name = f"{last_name}, {initials}"
            # full name for bibtex: write full name without initials
            full_name_bib = f"{last_name}, {' '.join(person.first_names + person.middle_names)}"
            authors_bib.append(full_name_bib)
            
            # Bold the specified author
            if highlight_author.lower() in ' '.join(person.first_names + person.last_names).lower():
                full_name = f"<strong>{full_name}</strong>"
                
            authors.append(full_name)

        # get the id number
        # ['id'] is C##NUMBER##, so we need to extract the number starting from the 2nd character
        fields['idnum'] = int(fields.get('id', 'C')[1:])

        # add authors to the field_bib
        field_bib['author'] = ' and '.join(authors_bib)

        # Generate the bibtex text
        bibtex_texts[id] = f" @{entry.type}{{{entry_key},\n" + \
                      '\n'.join([f"  {key} = {{{value}}}," for key, value in field_bib.items()]) + \
                      '\n}'

        
        # Construct the publication entry
        publication = {
            'id':  '[' + fields.get('id', '') + ']',
            'idnum': fields.get('idnum', ''),
            'volume': fields.get('volume', ''),
            'number': fields.get('number', ''),
            'pages': fields.get('pages', ''),
            'publisher': fields.get('publisher', ''),
            'url': fields.get('url', ''),
            'author': ', '.join(authors),
            'title': fields.get('title', ''),
            'journal': fields.get('journal', ''),
            'year': fields.get('year', ''),
            'year_num': int(fields.get('year', '')),
            'pdf': fields.get('pdf', ''),
            'video': fields.get('video', ''),         
            'code': fields.get('code', ''),
            'abstract': fields.get('abstract', ''),
            'bibtex': bibtex_texts[id],
            'review': fields.get('review', '')
        }
        
        publications.append(publication)

    # reorder the publications by id number (descending)
    publications = sorted(publications, key=lambda x: x['idnum'], reverse=True)

    # Write to YAML
    with open(yaml_file, 'w') as yaml_out:
        yaml.dump(publications, yaml_out, sort_keys=False, allow_unicode=True, default_flow_style=False)


def convert_bib_to_yaml_with_formatting_conference(bib_file, yaml_file, highlight_author):
    # Parse the .bib file
    bib_data = parse_file(bib_file)

    publications = []
    bibtex_texts = {}
    
    for entry_key, entry in bib_data.entries.items():
        # Extracting fields
        fields = entry.fields

        # create a field except for pdf, video, code, id, and abstract
        field_bib = {}
        for key, value in fields.items():
            if key not in ['pdf', 'video', 'code', 'id', 'abstract', 'review', 'award', 'slides']:
                field_bib[key] = value

        authors = []
        authors_bib = []
        # Format authors in AIAA style: "Family name, Initials"
        for person in entry.persons.get('author', []):
            last_name = person.last_names[0]
            initials = ''.join([name[0].upper() + '.' for name in person.first_names + person.middle_names])
            full_name = f"{last_name}, {initials}"
            # full name for bibtex: write full name without initials
            full_name_bib = f"{last_name}, {' '.join(person.first_names + person.middle_names)}"
            authors_bib.append(full_name_bib)
            
            # Bold the specified author
            if highlight_author.lower() in ' '.join(person.first_names + person.last_names).lower():
                full_name = f"<strong>{full_name}</strong>"
                
            authors.append(full_name)

        # get the id number
        # ['id'] is C##NUMBER##, so we need to extract the number starting from the 2nd character
        fields['idnum'] = int(fields.get('id', 'C')[1:])

        # add authors to the field_bib
        field_bib['author'] = ' and '.join(authors_bib)

        # Generate the bibtex text
        bibtex_texts[id] = f" @{entry.type}{{{entry_key},\n" + \
                      '\n'.join([f"  {key} = {{{value}}}," for key, value in field_bib.items()]) + \
                      '\n}'
        
        # Construct the publication entry
        publication = {
            'id':  '[' + fields.get('id', '') + ']',
            'idnum': fields.get('idnum', ''),
            'author': ', '.join(authors),
            'title': fields.get('title', ''),
            'journal': fields.get('journal', ''),
            'year': fields.get('year', ''),
            'year_num': int(fields.get('year', '')),
            'pdf': fields.get('pdf', ''),
            'url': fields.get('url', ''),
            'slides': fields.get('slides', ''),
            'video': fields.get('video', ''),         
            'code': fields.get('code', ''),
            'abstract': fields.get('abstract', ''),
            'award': fields.get('award', ''),
            'bibtex': bibtex_texts[id],
            'review': fields.get('review', '')
        }
        
        publications.append(publication)

    # reorder the publications by id number (descending)
    publications = sorted(publications, key=lambda x: x['idnum'], reverse=True)

    # Write to YAML
    with open(yaml_file, 'w') as yaml_out:
        yaml.dump(publications, yaml_out, sort_keys=False, allow_unicode=True, default_flow_style=False)

##################################################################################
# For magazines
# Convert the provided .bib file
convert_bib_to_yaml_with_formatting_maganize(
    'magazine.bib',  # Input .bib file
    '../_data/pubs_magazine.yml',  # Output .yml file
    'Keidai Iiyama'  # Highlighted author
)

##################################################################################
# For journals
# Convert the provided .bib file
convert_bib_to_yaml_with_formatting_journal(
    'journals.bib',  # Input .bib file
    '../_data/pubs_journal.yml',  # Output .yml file
    'Keidai Iiyama'  # Highlighted author
)

##################################################################################
# For preprints
# Convert the provided .bib file
convert_bib_to_yaml_with_formatting_journal(
    'preprints.bib',  # Input .bib file
    '../_data/pubs_preprints.yml',  # Output .yml file
    'Keidai Iiyama'  # Highlighted author
)

##################################################################################
# For conferences
# Convert the provided .bib file
convert_bib_to_yaml_with_formatting_conference(
    'conferences.bib',  # Input .bib file
    '../_data/pubs_conference.yml',  # Output .yml file
    'Keidai Iiyama'  # Highlighted author
)