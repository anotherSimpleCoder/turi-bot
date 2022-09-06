from moviepy.editor import concatenate_audioclips, AudioFileClip

class Evaluator:
    def __init__(self, words_list):
        self.words_list = words_list
        self.clip_paths = list()

    def eval(self):
        for w in self.words_list:
            match w:
                case 'turi':
                    self.clip_paths.append('turi.mp3')

                case 'ip':
                    self.clip_paths.append('ip.mp3')

    def combine_clips(self, out):
        clips = [AudioFileClip(c) for c in self.clip_paths]
        final_clip  = concatenate_audioclips(clips)
        final_clip.write_audiofile(out)