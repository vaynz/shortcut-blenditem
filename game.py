In function ## def OnKeyDown(self, key):

Search 
			self.RequestDropItem(False)
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

Add under

		if app.IsPressed(app.DIK_LCONTROL) and app.IsPressed(app.DIK_X):
			items_to_use = {71044, 71045}
			for i in xrange(player.INVENTORY_PAGE_SIZE * 4): 
				item_index = player.GetItemIndex(i)
				if item_index in items_to_use:
					net.SendItemUsePacket(i)
