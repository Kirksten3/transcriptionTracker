<?php
// requires that fileHelper.php be included before

class UI
{
	public static function CreateUserBoxes() {
		// reads from root
		$userObjectArray = FileHelper::ObjectizeFile('user.txt' );
		$len = count($userObjectArray);
		for ($i = 0; $i < $len; $i++) {
			// ensure image is 49x49 and make it a circle just in case it isn't
			echo "
			<div class='panel panel-default'>
				<div class='panel-body panel-select'>
			
					<img src='gui/assets/user_images/" . $userObjectArray[$i]->id . "'
					width='49px' height='49px' class='img-circle'/>
					<span>" . $userObjectArray[$i]->details . "</span>
					<imggroup>
						<img src='gui/assets/badge-slot.png' class='image-badge' />
						<img src='gui/assets/badge-slot.png' class='image-badge' />
						<img src='gui/assets/badge-slot.png' class='image-badge' />
					</imggroup>
			
				</div>
			</div>
			";
		}
	}
}
