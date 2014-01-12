#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: writeToFile
# Author: stephan sigg
# Description: USRP source write to file
# Generated: Sun Sep 23 15:19:48 2012
##################################################

from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import threading
import time
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="writeToFile")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.variable_function_probe_1 = variable_function_probe_1 = 0
		self.variable_function_probe_0 = variable_function_probe_0 = 0
		self.samp_rate = samp_rate = 32000
		self.receiveFrequency = receiveFrequency = 900000000

		##################################################
		# Blocks
		##################################################
		self.gr_probe_signal_f_1 = gr.probe_signal_f()
		self.gr_probe_signal_f_0 = gr.probe_signal_f()
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_0.win)
		def _variable_function_probe_1_probe():
			while True:
				val = self.gr_probe_signal_f_1.level()
				try: self.set_variable_function_probe_1(val)
				except AttributeError, e: pass
				# set sample rate
				time.sleep(1.0/(70))
				# in a first test with sample rate 1000 Hz about 15 values in a row have been identical
		_variable_function_probe_1_thread = threading.Thread(target=_variable_function_probe_1_probe)
		_variable_function_probe_1_thread.daemon = True
		_variable_function_probe_1_thread.start()
		def _variable_function_probe_0_probe():
			while True:
				val = self.gr_probe_signal_f_0.level()
				try: self.set_variable_function_probe_0(val)
				except AttributeError, e: pass
				# set sample rate
				time.sleep(1.0/(70))
				# in a first test with sample rate 1000 Hz about 15 values in a row have been identical
		_variable_function_probe_0_thread = threading.Thread(target=_variable_function_probe_0_probe)
		_variable_function_probe_0_thread.daemon = True
		_variable_function_probe_0_thread.start()
		self.uhd_usrp_source_0 = uhd.usrp_source(
			device_addr="",
			stream_args=uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),
		)
		self.uhd_usrp_source_0.set_samp_rate(samp_rate)
		self.uhd_usrp_source_0.set_center_freq(receiveFrequency, 0)
		self.uhd_usrp_source_0.set_gain(30, 0)
		self.gr_complex_to_float_0 = gr.complex_to_float(1)

		##################################################
		# Connections
		##################################################
		self.connect((self.uhd_usrp_source_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.uhd_usrp_source_0, 0), (self.gr_complex_to_float_0, 0))
		self.connect((self.gr_complex_to_float_0, 0), (self.gr_probe_signal_f_0, 0))
		self.connect((self.gr_complex_to_float_0, 1), (self.gr_probe_signal_f_1, 0))

	def get_variable_function_probe_1(self):
		return self.variable_function_probe_1

	def set_variable_function_probe_1(self, variable_function_probe_1):
		self.variable_function_probe_1 = variable_function_probe_1
		# print output for real part		
		fileRE = open ('outputRE', 'a')
		fileRE.write(str(self.variable_function_probe_1) + '\n')
		fileRE.close()
		#print self.variable_function_probe_1
		
	def get_variable_function_probe_0(self):
		return self.variable_function_probe_0

	def set_variable_function_probe_0(self, variable_function_probe_0):
		self.variable_function_probe_0 = variable_function_probe_0
		# print output for imaginary part
		fileIM = open ('outputIM', 'a')
		fileIM.write(str(self.variable_function_probe_0) + '\n')
		fileIM.close()

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
		self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

	def get_receiveFrequency(self):
		return self.receiveFrequency

	def set_receiveFrequency(self, receiveFrequency):
		self.receiveFrequency = receiveFrequency
		self.uhd_usrp_source_0.set_center_freq(self.receiveFrequency, 0)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	fileRE= open('outputRE','w')
	fileRE.write('Output Real Part\n')
	fileIM= open('outputIM','w')
	fileIM.write('Output Imaginary Part\n')
	fileRE.close()
	fileIM.close()
tb.Run(True)

