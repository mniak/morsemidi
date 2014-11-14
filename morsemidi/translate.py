import midiutil.MidiFile as midiutil
import morse as _morse

class Translator():

    def __init__(self):
        self.tempo = 120
        self.trackName = 'Morse Code'
        self.morse = _morse.Morse()

    def textToEvents(self, text):
        notes = []
        morseCode = self.morse.translate(text)
        space = 0
        for ch in morseCode:
            if ch is ',':
                space = 3
                continue
            elif ch is ';':
                space = 7
                continue
            elif ch in '-_':
                duration = 3
            elif ch is '.':
                duration = 1
            notes.append((space, 1))
            space = duration
            notes.append((space, 0))
            space = 1
        return notes

    def textToMidiFile(self, text, file_path):

        midi = midiutil.MIDIFile(1)

        track = 0
        time = 0

        # Add track name and tempo.
        midi.addTrackName(track,time, self.trackName)
        midi.addTempo(track, time, self.tempo)

        # Add a note. addNote expects the following information:
        channel = 0
        pitch = 60
        time = 0
        duration = 1
        volume = 100

        midi.addNote(track,channel,pitch,time,duration,volume)

        midiFile = open("output.mid", 'wb')
        midi.writeFile(midiFile)
        midi.close()