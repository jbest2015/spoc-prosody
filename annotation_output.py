from lxml import etree

def features_to_xml(features, text=None, tone=None, tone_confidence=None):
    root = etree.Element('speech')
    if text:
        etree.SubElement(root, 'text').text = text
    if tone:
        tone_elem = etree.SubElement(root, 'tone')
        tone_elem.set('type', tone)
        if tone_confidence:
            tone_elem.set('confidence', f"{int(tone_confidence*100)}%")
    for f in features:
        word_elem = etree.SubElement(root, 'word')
        if 'text' in f:
            etree.SubElement(word_elem, 'text').text = f['text']
        etree.SubElement(word_elem, 'pitch').text = str(f.get('pitch_note', 'N/A'))
        etree.SubElement(word_elem, 'volume').text = str(f.get('volume', 'N/A'))
        tb = f.get('time_between', None)
        if tb is not None:
            if tb < 0.15:
                tb_str = 'short'
            elif tb < 0.4:
                tb_str = 'moderate'
            elif tb < 0.8:
                tb_str = 'long'
            else:
                tb_str = 'very long'
        else:
            tb_str = 'normal'
        etree.SubElement(word_elem, 'time_between').text = tb_str
        # Volume variation
        vd = abs(f.get('volume_delta', 0))
        if vd < 0.05:
            vv = 'l'
        elif vd < 0.15:
            vv = 'm'
        else:
            vv = 'h'
        etree.SubElement(word_elem, 'volume_variation').text = vv
    return etree.tostring(root, pretty_print=True, encoding='unicode')


def features_to_compressed(features, words=None):
    out = []
    for i, f in enumerate(features):
        word = words[i] if words and i < len(words) else f'word{i+1}'
        pitch = f.get('pitch_note', 'N/A')
        volume = f.get('volume', 'N/A')
        # Volume variation
        vd = abs(f.get('volume_delta', 0))
        if vd < 0.05:
            vv = 'l'
        elif vd < 0.15:
            vv = 'm'
        else:
            vv = 'h'
        # Time between
        tb = f.get('time_between', None)
        if tb is not None:
            if tb < 0.15:
                tb_str = 's'
            elif tb < 0.4:
                tb_str = 'm'
            elif tb < 0.8:
                tb_str = 'l'
            else:
                tb_str = 'vl'
        else:
            tb_str = 'n'
        out.append(f"{word}({pitch},{volume},{vv},{tb_str})")
    return ' '.join(out) 