def asteroidCollision(asteroids):
    stack = []
    
    for asteroid in asteroids:
        # Process the current asteroid
        while stack and asteroid < 0 < stack[-1]:
            # Compare the top of the stack asteroid with current asteroid
            if stack[-1] < -asteroid:
                # Top asteroid is smaller, it explodes
                stack.pop()
                continue
            elif stack[-1] == -asteroid:
                # Both explode
                stack.pop()
            # Current asteroid explodes or both explode
            break
        else:
            # No collision, add asteroid to stack
            stack.append(asteroid)
    
    return stack

asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))  # Output: [5, 10]

asteroids = [8, -8]
print(asteroidCollision(asteroids))  # Output: []

asteroids = [10, 2, -5]
print(asteroidCollision(asteroids))  # Output: [10]

asteroids = [-2, -1, 1, 2]
print(asteroidCollision(asteroids))  # Output: [-2, -1, 1, 2]
