from pathlib import Path
import json

import pandas as pd
import fire


def get_subject_ids(data_path):
    participants = pd.read_csv(data_path/"participants.tsv", sep="\t")
    subject_ids = participants["participant_id"].unique().tolist()
    return subject_ids

def verify_eeg_all_subjects(data_path):
    for subject_id in get_subject_ids(data_path):
        subject_eeg_path = data_path / f"{subject_id}/eeg/{subject_id}_task-oc_eeg.edf"
        assert subject_eeg_path.exists(), f"EEG data not found for subject {subject_id}"
    print("EGG OK: All subjects found")

def verify_channels_and_sampling_all_subjects(data_path):
    for subject_id in get_subject_ids(data_path):
        eeg_metadata_path = data_path / f"{subject_id}/eeg/{subject_id}_task-oc_eeg.json"
        eeg_metadata = json.loads(eeg_metadata_path.read_text())
        sampling_freq = eeg_metadata["SamplingFrequency"]
        n_channels = eeg_metadata["EEGChannelCount"]
        assert sampling_freq == 500, f"Wrong sampling frequency, subject {subject_id}, got {sampling_freq}"
        assert n_channels == 20, f"Wrong n_channels, subject {subject_id}, got {n_channels}"
    print("OK: Channels and sampling frequecy correct")

def main(data_path):
    path = Path(data_path)
    verify_eeg_all_subjects(path)
    verify_channels_and_sampling_all_subjects(path)

if __name__ == "__main__":
  fire.Fire(main)