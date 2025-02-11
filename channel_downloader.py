#! /usr/bin/env python3

import time

import slack_token
import slacker
import channel


class ChannelDownloader(object):

    def __init__(self, sname, stoken):
        self.channel = channel.Channel()
        self.slack = slacker.Slacker(sname, stoken)

    def download(self, include_private=False):
        channel_types = ['public_channel']
        if include_private:
            channel_types.append('private_channel')
        channels = self.slack.get_all_channels(types=channel_types)
        self.channel.batch_upload(channels)


if __name__ == "__main__":
    channel_downloader = ChannelDownloader(
        "rands-leadership", slack_token.token)
    channel_downloader.download()
