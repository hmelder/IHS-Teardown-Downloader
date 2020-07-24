The IHS Teardown Analysis provides detailed Photos, PDFs and BOMs of various electronics. Very useful ... the problem is the price-tag. Well with this program you can legally obtain the full photo collection of all tear-downs.

#### Installation

```pip3 install ihs-dl```

#### Usage

```ihs-dl```

#### Screenshots
![TUI](https://raw.githubusercontent.com/DerNuntius/IHS-Teardown-Downloader/master/images/screenshot.png)
#### Brief Explaination

After some digging, I found a way to download the photos and PDFs.
The preview photos on the IHS Teardown Website only artificially limited and have a unique DeviceID and a PhotoID.
PDFs have a different retrieving system that I don't understand as of yet.
But I managed to use the query's ProductID to retrieve and download the associated photos. Each Photo has an associated JSON file (Title, Description etc). And after some HTML parsing, URL retrieving, photo downloading and renaming with the synced JSON we have full access to the IHS Teardown Archive.

#### Disclaimer and Copyright

The photos are publicly available and neither encrypted nor protected. There's no copyright infringement involved in any process. 
Be aware that every photo obtained is in the intellectual property of IHS Markit Ltd and may be illegal to redistribute.

