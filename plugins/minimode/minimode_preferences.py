# Copyright (C) 2010 Mathias Brodala
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import os, gtk
from xlgui.preferences import widgets
from xl import event, settings, xdg
from xl.nls import gettext as _

name = _('Mini Mode')
basedir = os.path.dirname(os.path.realpath(__file__))
ui = os.path.join(basedir, "minimode_preferences.ui")

class AlwaysOnTopPreference(widgets.CheckPreference):
    name = 'plugin/minimode/always_on_top'
    default = True

class ShowInPanelPreference(widgets.CheckPreference):
    name = 'plugin/minimode/show_in_panel'
    default = False

class OnAllDesktopsPreference(widgets.CheckPreference):
    name = 'plugin/minimode/on_all_desktops'
    default = True

class DisplayWindowDecorationsPreference(widgets.CheckPreference):
    name = 'plugin/minimode/display_window_decorations'
    default = True

class WindowDecorationTypePreference(widgets.ComboPreference,
        widgets.CheckConditional):
    name = 'plugin/minimode/window_decoration_type'
    default = 'full'
    condition_preference_name = 'plugin/minimode/display_window_decorations'

    def __init__(self, preferences, widget):
        widgets.ComboPreference.__init__(self, preferences, widget)
        widgets.CheckConditional.__init__(self)

class UseAlphaTransparencyPreference(widgets.CheckPreference):
    default = False
    name = 'plugin/minimode/use_alpha'

class TransparencyPreference(widgets.ScalePreference, widgets.CheckConditional):
    default = 0.3
    name = 'plugin/minimode/transparency'
    condition_preference_name = 'plugin/minimode/use_alpha'

    def __init__(self, preferences, widget):
        widgets.ScalePreference.__init__(self, preferences, widget)
        widgets.CheckConditional.__init__(self)

class SelectedControlsPreference(widgets.SelectionListPreference):
    name = 'plugin/minimode/selected_controls'
    default = ['previous', 'play_pause', 'next', 'playlist_button', 'progress_bar']
    items = [
        widgets.SelectionListPreference.Item(
            id='previous', title=_('Previous'),
            description=_('Go to the previous track')),
        widgets.SelectionListPreference.Item(
            id='play_pause', title=_('Play/Pause'),
            description=_('Start, pause or resume the playback')),
        widgets.SelectionListPreference.Item(
            id='stop', title=_('Stop'),
            description=_('Stop the playback')),
        widgets.SelectionListPreference.Item(
            id='next', title=_('Next'),
            description=_('Go to the next track')),
        widgets.SelectionListPreference.Item(
            id='track_selector', title=_('Track selector'),
            description=_('Simple track list selector')),
        widgets.SelectionListPreference.Item(
            id='progress_bar', title=_('Progress bar'),
            description=_('Playback progress and seeking')),
        widgets.SelectionListPreference.Item(
            id='volume', title=_('Volume'),
            description=_('Change the volume')),
        widgets.SelectionListPreference.Item(
            id='playlist_button', title=_('Playlist button'),
            description=_('Access the current playlist')),
        widgets.SelectionListPreference.Item(
            id='rating', title=_('Rating'),
            description=_('Select rating of the current track')),
        widgets.SelectionListPreference.Item(
            id='restore', title=_('Restore'),
            description=_('Restore main window'),
            fixed=True),
    ]

class TrackTitleFormatPreference(widgets.ComboEntryPreference):
    name = 'plugin/minimode/track_title_format'
    completion_items = {
        '$tracknumber': _('Track number'),
        '$title': _('Title'),
        '$artist': _('Artist'),
        '$composer': _('Composer'),
        '$album': _('Album'),
        '$__length': _('Length'),
        '$discnumber': _('Disc number'),
        '$__rating': _('Rating'),
        '$date': _('Date'),
        '$genre': _('Genre'),
        '$bitrate': _('Bitrate'),
        '$__location': _('Location'),
        '$filename': _('Filename'),
        '$__playcount': _('Play count'),
        '$__last_played': _('Last played'),
        '$bpm': _('BPM'),
    }
    preset_items = [
        # TRANSLATORS: Mini mode track selector title preset
        _('$tracknumber - $title'),
        # TRANSLATORS: Mini mode track selector title preset
        _('$title by $artist'),
        # TRANSLATORS: Mini mode track selector title preset
        _('$title ($__length)')
    ]
    default = _('$tracknumber - $title')
